(function(win,doc){
    'use strict';
    
    if(doc.querySelector('.btnDelPress')){
        let btnDelPress = doc.querySelectorAll('.btnDelPress');
        for(let i=0; i<btnDelPress.length; i++){
            btnDelPress[i].addEventListener('click',function(event){
                if(confirm('Tem certeza? Essas informações não poderão ser recuperadas.')){
                    return true;
                }else{
                    event.preventDefault();
                }
            })
        }
    }



    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form');
        function sendForm(event)
        {
            event.preventDefault();
            let data=new FormData(form);
            let ajax=new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN',token)
            ajax.onreadystatechange=function(){
                if(ajax.status===200 && ajax.readyState===4){
                    let result=doc.querySelector('#result');
                    result.innerHTML='Cadastro Concluido!'
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                }
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit',sendForm,false)
    }
})(window,document);