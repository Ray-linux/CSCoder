var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/hnjklpspuk24xx9d2wa7srdagxs8f2z5o81ooqu65wewqkkh/tinymce/6/tinymce.min.js";
document.head.appendChild(script);

script.onload = function(){
    tinymce.init({
        selector: '#id_source_code',
        plugins: 'a11ychecker advcode casechange export formatpainter editimage linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste advtable tableofcontents tinycomments tinymcespellchecker',
        toolbar: 'a11ycheck addcomment showcomments casechange checklist code export formatpainter image editimage pageembed permanentpen table tableofcontents',
        toolbar_mode: 'floating',
        tinycomments_mode: 'embedded',
        tinycomments_author: 'Author name',
      });

}
