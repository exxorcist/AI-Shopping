import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {searchAmazon, AmazonSearchResult} from 'unofficial-amazon-search';
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);


function Searchval() {
    var  x = document.getElementById("search").value;

    if (x === "dog") {
        window.open("/index.html");
    }

    if (x === "cat") {
        window.open("signin.html");
    }

    if(x){
      window.open("searchpage.html");
  }

}
// load other pages by specifying a page number
// or calling getNextPage()
searchAmazon('gamingpc', {page: 1, includeSponsoredResults: true}).then(data => {
 
  for (let i = 0; i < data.searchResults.length; i++)  {
                                        //for (let j = 0; j < 2; j++)  {
                                        console.log(data.searchResults[i].imageUrl);//}
  }
                                        const a1 = String(data.searchResults[0].imageUrl);
                                        const image = document.getElementById("event-1");
                                        
                                        image.src = a1;
});


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
