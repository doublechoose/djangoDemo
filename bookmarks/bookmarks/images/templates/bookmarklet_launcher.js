(function(){
    // 防止多次点击造成多个窗口
    if(window.bookmarklet!==undefined){
        bookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script')).src='http://127.0.0.1:8000/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();