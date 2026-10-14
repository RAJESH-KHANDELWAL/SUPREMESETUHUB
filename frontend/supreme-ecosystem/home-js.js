/* SUPREME ECOSYSTEM HOME JS — extracted from the existing SUPREME homepage source; no remote loader. */

/* Original inline script 1 */
(function(){
  "use strict";
  var control=document.getElementById("supreme-language");
  if(!control) return;
  var labels={en:{lang:"en"},hi:{lang:"hi"},hinglish:{lang:"hi-Latn"}};
  function apply(value){
    var item=labels[value]||{lang:value};
    document.documentElement.setAttribute("lang",item.lang);
    document.documentElement.setAttribute("data-supreme-language",value);
    if(document.body) document.body.setAttribute("data-supreme-language",value);
    try{localStorage.setItem("supreme-language",value);}catch(error){}
  }
  var saved="hinglish";
  try{saved=localStorage.getItem("supreme-language")||"hinglish";}catch(error){}
  if(!labels[saved]) saved="hinglish";
  control.value=saved;apply(saved);
  control.addEventListener("change",function(){apply(control.value);document.dispatchEvent(new CustomEvent("supreme:languagechange",{detail:{language:control.value}}));});
  document.addEventListener("DOMContentLoaded",function(){document.dispatchEvent(new CustomEvent("supreme:languagechange",{detail:{language:control.value}}));});
  document.dispatchEvent(new CustomEvent("supreme:languagechange",{detail:{language:control.value}}));
})();

/* Original inline script 2 */
(function(){
  "use strict";
  var hub=document.getElementById("supreme-social-hub");
  if(!hub) return;
  var translations={
    en:{
      "YOUR DIGITAL COMMUNITY":"YOUR DIGITAL COMMUNITY","Connect. Share. Grow.":"Connect. Share. Grow.","Social updates and professional opportunities in one place.":"Social updates and professional opportunities in one place.",
      "STORIES":"STORIES","Add story":"Add story","Ideas":"Ideas","Business":"Business","Learning":"Learning","Community":"Community",
      "Share an update, idea or opportunity":"Share an update, idea or opportunity","What would you like to share with your community?":"What would you like to share with your community?",
      "PUBLISH POST":"PUBLISH POST","Front-end preview: posts appear in this browser view only until connected to a secure backend.":"Front-end preview: posts appear in this browser view only until connected to a secure backend.",
      "Social Feed":"Social Feed","Professional Network":"Professional Network","Services & Opportunities":"Services & Opportunities","Messages":"Messages","Communities":"Communities","🏠 Social Feed":"🏠 Social Feed","⭕ Stories":"⭕ Stories","💬 Messages":"💬 Messages","💼 Professional Network":"💼 Professional Network","👥 Communities":"👥 Communities","🛍️ Services & Opportunities":"🛍️ Services & Opportunities",
      "Messages":"Messages","Messaging interface foundation.":"Messaging interface foundation.","Your conversations will appear here":"Your conversations will appear here",
      "Real-time delivery, private chat and notifications need authenticated backend services.":"Real-time delivery, private chat and notifications need authenticated backend services.",
      "Build your presence":"Build your presence","Trust & transparency":"Trust & transparency","Connect a business, services and projects":"Connect a business, services and projects"
    },
    hi:{
      "YOUR DIGITAL COMMUNITY":"आपका डिजिटल समुदाय","Connect. Share. Grow.":"जुड़ें। साझा करें। आगे बढ़ें।","Social updates and professional opportunities in one place.":"सोशल अपडेट और प्रोफेशनल अवसर—एक ही जगह।",
      "STORIES":"स्टोरीज़","Add story":"स्टोरी जोड़ें","Ideas":"विचार","Business":"व्यवसाय","Learning":"सीखना","Community":"समुदाय",
      "Share an update, idea or opportunity":"अपडेट, विचार या अवसर साझा करें","What would you like to share with your community?":"आप अपने समुदाय के साथ क्या साझा करना चाहेंगे?",
      "PUBLISH POST":"पोस्ट प्रकाशित करें","Front-end preview: posts appear in this browser view only until connected to a secure backend.":"फ्रंटएंड प्रीव्यू: सुरक्षित बैकएंड से जुड़ने तक पोस्ट केवल इसी ब्राउज़र में दिखेंगी।",
      "Social Feed":"सोशल फ़ीड","Professional Network":"प्रोफेशनल नेटवर्क","Services & Opportunities":"सेवाएँ और अवसर","Messages":"संदेश","Communities":"समुदाय","🏠 Social Feed":"🏠 सोशल फ़ीड","⭕ Stories":"⭕ स्टोरीज़","💬 Messages":"💬 संदेश","💼 Professional Network":"💼 प्रोफेशनल नेटवर्क","👥 Communities":"👥 समुदाय","🛍️ Services & Opportunities":"🛍️ सेवाएँ और अवसर",
      "Messaging interface foundation.":"मैसेजिंग इंटरफ़ेस का आधार।","Your conversations will appear here":"आपकी बातचीत यहाँ दिखाई देगी",
      "Real-time delivery, private chat and notifications need authenticated backend services.":"रीयल-टाइम संदेश, निजी चैट और नोटिफ़िकेशन के लिए सुरक्षित लॉगिन वाला बैकएंड चाहिए।",
      "Build your presence":"अपनी पहचान बनाएँ","Trust & transparency":"विश्वास और पारदर्शिता"
    },
    hinglish:{
      "YOUR DIGITAL COMMUNITY":"AAPKI DIGITAL COMMUNITY","Connect. Share. Grow.":"CONNECT KARO. SHARE KARO. GROW KARO.","Social updates and professional opportunities in one place.":"Social updates aur professional opportunities — ek hi jagah.",
      "STORIES":"STORIES","Add story":"Story add karo","Ideas":"Ideas","Business":"Business","Learning":"Learning","Community":"Community",
      "Share an update, idea or opportunity":"Update, idea ya opportunity share karo","What would you like to share with your community?":"Apni community ke saath kya share karna chahoge?",
      "PUBLISH POST":"POST PUBLISH KARO","Front-end preview: posts appear in this browser view only until connected to a secure backend.":"Front-end preview: secure backend connect hone tak posts sirf isi browser mein dikhenge.",
      "Social Feed":"Social Feed","Professional Network":"Professional Network","Services & Opportunities":"Services & Opportunities","Messages":"Messages","Communities":"Communities",
      "Messaging interface foundation.":"Messaging interface ka foundation.","Your conversations will appear here":"Aapki conversations yahan dikhenge",
      "Real-time delivery, private chat and notifications need authenticated backend services.":"Real-time messages, private chat aur notifications ke liye secure login wala backend chahiye.",
      "Build your presence":"Apni presence build karo","Trust & transparency":"Trust aur transparency"
    }
  };
  function applyHubLanguage(language){
    var dictionary=translations[language]||translations.hinglish;
    var walker=document.createTreeWalker(hub,NodeFilter.SHOW_TEXT);
    var nodes=[],node;
    while((node=walker.nextNode())) nodes.push(node);
    nodes.forEach(function(textNode){
      if(typeof textNode.__sshOriginalText==="undefined") textNode.__sshOriginalText=textNode.nodeValue;
      var original=textNode.__sshOriginalText;
      var key=original.trim();
      textNode.nodeValue=dictionary[key]?original.replace(key,dictionary[key]):original;
    });
    var placeholders={
      en:{"Search people, posts, services...":"Search people, posts, services...","Write a comment...":"Write a comment..."},
      hi:{"Search people, posts, services...":"लोग, पोस्ट और सेवाएँ खोजें...","Write a comment...":"कमेंट लिखें..."},
      hinglish:{"Search people, posts, services...":"People, posts, services search karo...","Write a comment...":"Comment likho..."}
    }[language]||{};
    hub.querySelectorAll("input[placeholder],textarea[placeholder]").forEach(function(el){
      if(typeof el.__sshOriginalPlaceholder==="undefined")el.__sshOriginalPlaceholder=el.getAttribute("placeholder");
      var key=el.__sshOriginalPlaceholder;el.setAttribute("placeholder",placeholders[key]||key);
    });
    hub.setAttribute("lang",language==="hi"?"hi":language==="en"?"en":"hi-Latn");
  }
  document.addEventListener("supreme:languagechange",function(e){applyHubLanguage(e.detail&&e.detail.language);});
  var currentLanguage="hinglish";try{currentLanguage=localStorage.getItem("supreme-language")||"hinglish";}catch(error){}applyHubLanguage(currentLanguage);
  function showView(name){
    hub.querySelectorAll("[data-ssh-panel]").forEach(function(p){p.classList.toggle("is-visible",p.getAttribute("data-ssh-panel")===name);});
    hub.querySelectorAll("[data-ssh-view]").forEach(function(b){b.classList.toggle("is-active",b.getAttribute("data-ssh-view")===name);});
  }
  hub.addEventListener("click",function(e){
    var view=e.target.closest("[data-ssh-view]");
    if(view){showView(view.getAttribute("data-ssh-view"));return;}
    var react=e.target.closest("[data-ssh-react]");
    if(react){var count=react.querySelector("span");var liked=react.classList.toggle("is-liked");count.textContent=String(Math.max(0,Number(count.textContent)+(liked?1:-1)));react.firstChild.textContent=liked?"♥ LIKE ":"♡ LIKE ";return;}
    var comment=e.target.closest("[data-ssh-comment]");
    if(comment){var box=comment.closest(".ssh-post").querySelector(".ssh-comment-box");box.hidden=!box.hidden;return;}
    var submit=e.target.closest("[data-ssh-submit-comment]");
    if(submit){var input=submit.parentElement.querySelector("input");if(input.value.trim()){var note=document.createElement("p");note.className="ssh-local-comment";note.textContent="You: "+input.value.trim();submit.parentElement.before(note);input.value="";}return;}
    var share=e.target.closest("[data-ssh-share]");
    if(share){if(navigator.share){navigator.share({title:"SUPREME SETU HUB",text:"Explore this community update."}).catch(function(){});}else{var old=share.textContent;share.textContent="✓ READY TO SHARE";setTimeout(function(){share.textContent=old;},1600);}return;}
    var demo=e.target.closest("[data-ssh-demo]");
    if(demo){demo.textContent="COMING SOON";demo.disabled=true;}
  });
  hub.addEventListener("submit",function(e){
    if(e.target.id!=="ssh-post-form") return;
    e.preventDefault();
    var field=hub.querySelector("#ssh-post-text"), value=field.value.trim();
    if(!value) return;
    var article=document.createElement("article");article.className="ssh-post";
    var author=document.createElement("div");author.className="ssh-post-author";
    var avatar=document.createElement("span");avatar.className="ssh-avatar";avatar.textContent="RK";
    var info=document.createElement("div");var name=document.createElement("strong");name.textContent="DR RAJESH KHANDELWAL IBC";var meta=document.createElement("small");meta.textContent="Just now · Local preview";info.append(name,meta);author.append(avatar,info);
    var body=document.createElement("p");body.textContent=value;
    var actions=document.createElement("div");actions.className="ssh-post-actions";actions.innerHTML='<button type="button" data-ssh-react>♡ LIKE <span>0</span></button><button type="button" data-ssh-comment>💬 COMMENT</button><button type="button" data-ssh-share>↗ SHARE</button>';
    var comments=document.createElement("div");comments.className="ssh-comment-box";comments.hidden=true;comments.innerHTML='<input type="text" placeholder="Write a comment..." aria-label="Write a comment"><button type="button" data-ssh-submit-comment>POST</button>';
    article.append(author,body,actions,comments);hub.querySelector("#ssh-feed").prepend(article);field.value="";
  });
})();

/* Original inline script 3 */
(function(){
  "use strict";
  var languageSelect=document.getElementById("supreme-language");
  var status=document.getElementById("sglt-status");
  var originalText=document.getElementById("sglt-original");
  var translatedText=document.getElementById("sglt-translated");
  var startButton=document.getElementById("sglt-start");
  var stopButton=document.getElementById("sglt-stop");
  var sourceSelect=document.getElementById("sglt-source");
  var speakToggle=document.getElementById("sglt-speak");
  var programmingList=document.getElementById("sglt-programming-list");
  var recognition=null,active=false,translating=false;
  var originalNodes=[];
  function targetCode(){return languageSelect.value==="hinglish"?"hi":languageSelect.value;}
  function safeStatus(message){if(status)status.textContent=message;}
  function api(path,body){
    return fetch("https://supremesetuhub-3v4e.onrender.com/api/v1/languages/"+path,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)}).then(function(response){
      return response.json().then(function(data){if(!response.ok)throw new Error((data.detail&&data.detail.message)||data.detail||"Translation request failed");return data;});
    });
  }
  function addLanguageOptions(items){
    if(!languageSelect)return;
    var existing={};Array.prototype.forEach.call(languageSelect.options,function(o){existing[o.value]=true;});
    items.forEach(function(item){
      if(!existing[item.code]){
        var option=document.createElement("option");option.value=item.code;
        option.textContent=item.native_name+" — "+item.name;
        languageSelect.appendChild(option);existing[item.code]=true;
      }
      if(sourceSelect&&!Array.prototype.some.call(sourceSelect.options,function(o){return o.value===item.code;})){
        var speechOption=document.createElement("option");speechOption.value=item.code;
        speechOption.textContent=item.native_name+" — "+item.name;sourceSelect.appendChild(speechOption);
      }
    });
  }
  function collectOriginalNodes(){
    originalNodes=[];
    var walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,{
      acceptNode:function(node){
        var parent=node.parentElement;
        if(!parent||parent.closest("script,style,noscript,textarea,select,option,code,pre,[contenteditable=true],.sglt-caption,#sglt-status"))return NodeFilter.FILTER_REJECT;
        if(!node.nodeValue.trim())return NodeFilter.FILTER_REJECT;
        if(typeof node.__sgltOriginal==="undefined")node.__sgltOriginal=node.nodeValue;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var n;while((n=walker.nextNode()))originalNodes.push(n);
  }
  async function translateWholePage(){
    var target=targetCode();
    if(target==="en"){
      collectOriginalNodes();originalNodes.forEach(function(n){n.nodeValue=n.__sgltOriginal;});
      safeStatus("English selected. Original page text restored.");return;
    }
    collectOriginalNodes();
    safeStatus("Translating page text…");
    var translatedCount=0;
    try{
      for(var i=0;i<originalNodes.length;i+=40){
        var nodes=originalNodes.slice(i,i+40);
        var texts=nodes.map(function(n){return n.__sgltOriginal;});
        var result=await api("translate/batch",{texts:texts,source:"auto",target:target});
        result.translated_texts.forEach(function(value,index){nodes[index].nodeValue=value;translatedCount++;});
      }
      safeStatus("Page text translated ("+translatedCount+" text segments). Dynamic content may need translation again.");
    }catch(error){
      safeStatus("Translation unavailable: "+error.message+". Configure SUPREME_TRANSLATION_API_URL on the server.");
    }
  }
  function mapSpeechLanguage(code){
    var map={hi:"hi-IN",gu:"gu-IN",bn:"bn-IN",ta:"ta-IN",te:"te-IN",mr:"mr-IN",pa:"pa-IN",ur:"ur-PK",ar:"ar-SA",en:"en-US",es:"es-ES",fr:"fr-FR",de:"de-DE",zh:"zh-CN",ja:"ja-JP",ko:"ko-KR",pt:"pt-BR",ru:"ru-RU"};
    return map[code]||code;
  }
  async function translateUtterance(text){
    originalText.textContent=text;
    try{
      var result=await api("translate",{text:text,source:"auto",target:targetCode()});
      translatedText.textContent=result.translated_text;
      if(speakToggle.checked&&"speechSynthesis" in window){
        window.speechSynthesis.cancel();
        var utterance=new SpeechSynthesisUtterance(result.translated_text);
        utterance.lang=mapSpeechLanguage(targetCode());window.speechSynthesis.speak(utterance);
      }
    }catch(error){translatedText.textContent="Translation unavailable: "+error.message;}
  }
  function stopRecognition(){
    active=false;stopButton.disabled=true;startButton.disabled=false;
    if(recognition){try{recognition.stop();}catch(error){}}
    recognition=null;
  }
  startButton.addEventListener("click",function(){
    var SpeechRecognition=window.SpeechRecognition||window.webkitSpeechRecognition;
    if(!SpeechRecognition){translatedText.textContent="Live speech recognition is not supported in this browser. Try a current Chrome or Edge browser.";return;}
    if(!window.isSecureContext){translatedText.textContent="Microphone access requires HTTPS or localhost.";return;}
    recognition=new SpeechRecognition();recognition.continuous=true;recognition.interimResults=true;
    recognition.lang=sourceSelect.value==="auto"?"en-US":mapSpeechLanguage(sourceSelect.value);
    recognition.onresult=function(event){
      var finalText="";
      for(var i=event.resultIndex;i<event.results.length;i++){
        var transcript=event.results[i][0].transcript;
        if(event.results[i].isFinal)finalText+=transcript;
        else originalText.textContent=transcript+" …";
      }
      if(finalText.trim())translateUtterance(finalText.trim());
    };
    recognition.onerror=function(event){translatedText.textContent="Speech recognition: "+event.error;};
    recognition.onend=function(){if(active){try{recognition.start();}catch(error){stopRecognition();}}};
    try{recognition.start();active=true;startButton.disabled=true;stopButton.disabled=false;translatedText.textContent="Listening…";}catch(error){translatedText.textContent="Could not start microphone: "+error.message;}
  });
  stopButton.addEventListener("click",stopRecognition);
  if(languageSelect)languageSelect.addEventListener("change",translateWholePage);
  fetch("https://supremesetuhub-3v4e.onrender.com/api/v1/languages/catalog").then(function(r){if(!r.ok)throw new Error("Catalogue unavailable");return r.json();}).then(function(data){
    addLanguageOptions(data.human_languages||[]);
    if(programmingList)programmingList.textContent=(data.programming_languages||[]).map(function(x){return x.name;}).join(" · ");
    safeStatus(data.translation_provider_configured?"Language catalogue ready. Translation provider configured.":"Language catalogue ready. Live translation needs a server translation provider.");
  }).catch(function(){safeStatus("Language catalogue unavailable; built-in options remain available.");});
})();