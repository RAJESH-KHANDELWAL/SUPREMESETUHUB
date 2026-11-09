"""Safe Wi-Fi visibility scanner for SUPREME.

Lists SSIDs broadcast to the local device and security/signal metadata only.
It never extracts, guesses, cracks, stores, or reveals Wi-Fi passwords and does
not connect to networks. "Free" means only that the network advertises open
authentication; it does not prove the network is trustworthy or has internet.
"""
from __future__ import annotations
import platform, re, subprocess
from typing import Any

def scan_visible_wifi() -> dict[str, Any]:
    if platform.system() != "Windows":
        return {"status":"UNSUPPORTED_PLATFORM","networks":[],"message":"This adapter currently supports Windows netsh only."}
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            capture_output=True, text=True, timeout=12, check=False,
            encoding="utf-8", errors="replace",
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"status":"SCAN_FAILED","networks":[],"message":type(exc).__name__}
    if result.returncode != 0:
        return {"status":"SCAN_UNAVAILABLE","networks":[],"message":"Windows WLAN scan failed; check Wi-Fi adapter/permissions."}
    networks=[]
    current=None
    for line in result.stdout.splitlines():
        s=line.strip()
        m=re.match(r"SSID\s+\d+\s*:\s*(.*)$",s,re.I)
        if m:
            if current: networks.append(current)
            current={"ssid":m.group(1).strip() or "<hidden SSID>","authentication":"UNKNOWN","encryption":"UNKNOWN","signal_percent":None,"availability":"VISIBLE","free_open_network":False}
            continue
        if current:
            m=re.match(r"Authentication\s*:\s*(.*)$",s,re.I)
            if m: current["authentication"]=m.group(1).strip()
            m=re.match(r"Encryption\s*:\s*(.*)$",s,re.I)
            if m: current["encryption"]=m.group(1).strip()
            m=re.match(r"Signal\s*:\s*(\d+)%",s,re.I)
            if m: current["signal_percent"]=int(m.group(1))
    if current: networks.append(current)
    for n in networks:
        n["free_open_network"] = n["authentication"].lower() in {"open","none"}
        n["password_status"] = "NO_PASSWORD_REQUIRED_ADVERTISED" if n["free_open_network"] else "PASSWORD_NOT_CHECKED"
        n["internet_status"] = "NOT_TESTED"
    return {"status":"OK","networks":networks,"count":len(networks),"passwords_collected":False,"auto_connect":False}
