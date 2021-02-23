// Create Socket Instance
const socket = io("http://localhost:3000/upbit");

// On Event, Wait for 'connect' emit.
socket.on("connect", ()=>{
  console.log("[connect]");
});

// On Event, Wait for 'disconnect' emit.
socket.on("disconnect", ()=>{
  console.log("[disconnect]");
});

// On Event, Wait for 'rcv_price' emit.
socket.on("rcv_price", ({ tickers, markets, size })=>{
  const ticker_list = document.querySelector("#tickerlist");
  
  const ul = document.createElement("ul");
  tickers.forEach((t)=>{
    const li = ul.appendChild(document.createElement("li"));
    li.appendChild(document.createTextNode(t));
    li.appendChild(document.createTextNode(":"));
    li.appendChild(document.createTextNode(markets[t]||0));
  });
  
  ticker_list.innerHTML = ul.innerHTML;
  
  console.log({ tickers, markets, size });
});
