const password = prompt("Пароль проєкту:")||"qwerty123";
const chat   = document.getElementById('chat');
const inp    = document.getElementById('inp');
const sendBtn= document.getElementById('send');

sendBtn.onclick = () => sendMsg();

async function sendMsg(){
  const msg = inp.value.trim(); if(!msg) return;
  addBubble(msg,"user");
  inp.value="";
  const res = await fetch("http://localhost:8000/generate",{
    method:"POST",
    headers:{"Content-Type":"application/json","X-Password":password},
    body: JSON.stringify({prompt:msg})
  });
  const reader = res.body.getReader();
  let out = ""; addBubble("","assistant");
  while(true){
    const {done,value} = await reader.read();
    if(done) break;
    out += new TextDecoder().decode(value);
    chat.lastElementChild.textContent = out;
  }
}
function addBubble(text,who){
  const div = document.createElement('div');
  div.textContent = text;
  div.style.marginBottom="4px";
  div.style.color = (who==="user")?"#7fd":"#ccc";
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}
