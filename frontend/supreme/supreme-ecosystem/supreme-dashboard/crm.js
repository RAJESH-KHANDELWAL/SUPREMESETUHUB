"use strict";
(() => {
  const API = "https://supremesetuhub-3v4e.onrender.com";
  let token = localStorage.getItem("supreme_token") || "";
  let contacts = [];
  let tasks = [];
  const $ = (id) => document.getElementById(id);
  const esc = (value) => String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"
  }[char]));
  const notice = (message, kind = "") => {
    $("notice").textContent = message;
    $("notice").className = "notice" + (kind ? " " + kind : "");
  };
  const authFetch = async (path, options = {}) => {
    const response = await fetch(API + path, {
      ...options,
      headers: {
        "Accept": "application/json",
        ...(options.body ? {"Content-Type":"application/json"} : {}),
        ...(options.headers || {}),
        "Authorization": "Bearer " + token
      }
    });
    const data = await response.json().catch(() => ({}));
    if (response.status === 401 || response.status === 403) {
      if (response.status === 401) {
        localStorage.removeItem("supreme_token");
        window.location.replace("signin.html");
      }
      throw new Error(data.detail || "This account is not authorized for this CRM action.");
    }
    if (!response.ok) throw new Error(data.detail || data.message || ("Request failed: " + response.status));
    return data;
  };
  const emptyRow = (cols, message) => '<tr><td colspan="' + cols + '">' + esc(message) + "</td></tr>";
  const optionLabel = (contact) => [contact.full_name, contact.organization, contact.phone].filter(Boolean).join(" · ");

  async function loadSummary() {
    const [report, quality] = await Promise.all([
      authFetch("/api/v1/crm/reports/summary"),
      authFetch("/api/v1/crm/quality/review-queue?limit=500")
    ]);
    $("totalContacts").textContent = report.report?.total_contacts ?? "—";
    $("flaggedContacts").textContent = quality.flagged_count ?? "—";
    $("unverifiedContacts").textContent = quality.unverified_count ?? "—";
    $("overdueFollowups").textContent = report.report?.overdue_follow_ups ?? "—";
    const rows = quality.data || [];
    $("qualityRows").innerHTML = rows.length ? rows.map((item) => {
      const flags = (item.flags || []).map((flag) => '<span class="flag">' + esc(flag.field) + ": " + esc(flag.code.replaceAll("_"," ").toLowerCase()) + "</span>").join("");
      const badgeClass = item.quality_label === "INCOMPLETE" ? " incomplete" : "";
      return '<tr><td><strong>' + esc(item.full_name) + '</strong><br><small>' + esc(item.phone || "") + '</small></td><td><span class="quality-badge' + badgeClass + '">' + esc(item.quality_score) + '/100</span></td><td><div class="flag-list">' + flags + '</div></td><td>' + esc((item.next_action || "").replaceAll("_"," ").toLowerCase()) + "</td></tr>";
    }).join("") : emptyRow(4, "No flagged contacts in this review batch.");
  }

  function populateContactSelects() {
    const selects = [$("taskContact"), $("activityContact")];
    for (const select of selects) {
      const previous = select.value;
      const first = select.id === "taskContact" ? '<option value="">No contact linked</option>' : '<option value="">Choose contact</option>';
      select.innerHTML = first + contacts.map((contact) => '<option value="' + esc(contact.contact_id) + '">' + esc(optionLabel(contact)) + "</option>").join("");
      if (contacts.some((contact) => contact.contact_id === previous)) select.value = previous;
    }
  }

  function renderContacts() {
    const query = $("contactSearch").value.trim().toLowerCase();
    const filtered = contacts.filter((contact) => [
      contact.full_name, contact.organization, contact.phone, contact.email, contact.city
    ].some((value) => String(value || "").toLowerCase().includes(query)));
    $("contactRows").innerHTML = filtered.length ? filtered.map((contact) =>
      "<tr><td><strong>" + esc(contact.full_name) + "</strong></td><td>" + esc(contact.organization || "—") +
      "</td><td>" + esc(contact.phone || "—") + (contact.whatsapp_phone ? "<br><small>WhatsApp: " + esc(contact.whatsapp_phone) + "</small>" : "") +
      "</td><td>" + esc(contact.email || "—") + "</td><td>" + esc(contact.city || "—") +
      "</td><td>" + esc(contact.verification_status || "UNVERIFIED") + "</td></tr>"
    ).join("") : emptyRow(6, "No matching contacts.");
  }

  async function loadContacts() {
    const result = await authFetch("/api/v1/crm/contacts?limit=500");
    contacts = result.data || [];
    populateContactSelects();
    renderContacts();
  }

  function renderTasks() {
    $("taskRows").innerHTML = tasks.length ? tasks.map((task) => {
      const next = task.status === "OPEN" ? "IN_PROGRESS" : task.status === "IN_PROGRESS" ? "DONE" : "OPEN";
      const actionLabel = task.status === "DONE" ? "Reopen" : task.status === "IN_PROGRESS" ? "Mark done" : "Start";
      return '<article class="task"><div><strong>' + esc(task.title) + '</strong><small>' + esc(task.item_type) + " · " + esc(task.status) +
        (task.due_at ? " · Due " + esc(task.due_at) : "") + '</small><small>' + esc(task.details || "") +
        '</small></div><div class="task-controls"><button class="button secondary" data-task-id="' + esc(task.item_id) +
        '" data-task-status="' + esc(next) + '">' + esc(actionLabel) + "</button></div></article>";
    }).join("") : '<div class="empty">No daily work items yet. Add your first task above.</div>';
  }

  async function loadBriefing() {
    const result = await authFetch("/api/v1/crm/daily/briefing");
    const summary = result.summary || {};
    $("dailySummary").innerHTML = '<span class="daily-chip">Open: ' + esc(summary.open ?? 0) +
      '</span><span class="daily-chip">In progress: ' + esc(summary.in_progress ?? 0) +
      '</span><span class="daily-chip">Done: ' + esc(summary.done ?? 0) + "</span>";
    tasks = result.items || [];
    renderTasks();
  }

  async function loadTimeline() {
    const contactId = $("activityContact").value;
    if (!contactId) {
      $("timelineRows").innerHTML = '<p class="muted">Choose a contact first.</p>';
      return;
    }
    const result = await authFetch("/api/v1/crm/contacts/" + encodeURIComponent(contactId) + "/timeline?limit=100");
    const rows = result.data || [];
    $("timelineRows").innerHTML = rows.length ? rows.map((item) =>
      '<article class="timeline-item"><strong>' + esc(item.activity_type) + " · " + esc(item.summary) +
      '</strong><p>' + esc(item.details || "") + (item.outcome ? "<br><b>Outcome:</b> " + esc(item.outcome) : "") +
      (item.next_follow_up_at ? "<br><b>Next follow-up:</b> " + esc(item.next_follow_up_at) : "") +
      '</p><small>' + esc(item.created_at || "") + "</small></article>"
    ).join("") : '<p class="muted">No activity has been recorded for this contact yet.</p>';
  }

  async function refreshAll() {
    $("refreshBtn").disabled = true;
    notice("Loading CRM data…");
    try {
      await Promise.all([loadSummary(), loadContacts(), loadBriefing()]);
      notice("CRM data refreshed. Quality checks are rule-based; they do not prove identity or reachability.", "success");
    } catch (error) {
      notice(error.message || "Could not load CRM data. Confirm backend deployment and your access.", "error");
    } finally {
      $("refreshBtn").disabled = false;
    }
  }

  $("refreshBtn").addEventListener("click", refreshAll);
  $("reloadBriefing").addEventListener("click", () => loadBriefing().catch((error) => notice(error.message, "error")));
  $("loadTimeline").addEventListener("click", () => loadTimeline().catch((error) => notice(error.message, "error")));
  $("activityContact").addEventListener("change", () => {
    $("timelineRows").innerHTML = '<p class="muted">Select “Load selected contact” to retrieve the timeline.</p>';
  });
  $("contactSearch").addEventListener("input", renderContacts);
  $("logoutBtn").addEventListener("click", () => {
    localStorage.removeItem("supreme_token");
    window.location.replace("signin.html");
  });

  $("taskForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const dueValue = $("taskDue").value;
    const payload = {
      title: $("taskTitle").value.trim(),
      item_type: $("taskType").value,
      details: $("taskDetails").value.trim(),
      contact_id: $("taskContact").value || null,
      due_at: dueValue ? new Date(dueValue).toISOString() : null
    };
    try {
      await authFetch("/api/v1/crm/daily/items", {method:"POST", body:JSON.stringify(payload)});
      $("taskForm").reset();
      await loadBriefing();
      notice("Daily work item saved.", "success");
    } catch (error) { notice(error.message || "Could not save task.", "error"); }
  });

  $("taskRows").addEventListener("click", async (event) => {
    const button = event.target.closest("button[data-task-id]");
    if (!button) return;
    button.disabled = true;
    try {
      await authFetch("/api/v1/crm/daily/items/" + encodeURIComponent(button.dataset.taskId), {
        method:"PATCH", body:JSON.stringify({status:button.dataset.taskStatus})
      });
      await loadBriefing();
      notice("Task status updated.", "success");
    } catch (error) { notice(error.message || "Could not update task.", "error"); }
    finally { button.disabled = false; }
  });

  $("activityForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const dueValue = $("activityFollowup").value;
    const payload = {
      contact_id: $("activityContact").value,
      activity_type: $("activityType").value,
      summary: $("activitySummary").value.trim(),
      details: $("activityDetails").value.trim(),
      outcome: $("activityOutcome").value.trim(),
      next_follow_up_at: dueValue ? new Date(dueValue).toISOString() : null
    };
    try {
      await authFetch("/api/v1/crm/activities", {method:"POST", body:JSON.stringify(payload)});
      $("activitySummary").value = "";
      $("activityDetails").value = "";
      $("activityOutcome").value = "";
      $("activityFollowup").value = "";
      await loadTimeline();
      notice("Activity saved to the contact timeline.", "success");
    } catch (error) { notice(error.message || "Could not save activity.", "error"); }
  });

  if (!token) {
    window.location.replace("signin.html");
    return;
  }
  refreshAll();
})();
