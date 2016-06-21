var lista = document.getElementsByClassName("opTresc");

for (var i = 0; i < lista.length; ++i){	
  	var comment = lista[i].firstElementChild.innerHTML;
	checkComment(comment, i);
}


function checkComment(comment, nr){
		var webpy = 'http://0.0.0.0:8080/?callback=?';
		var webpy2 = 'http://0.0.0.0:8080/';
		var resp = "";
		//~ return 
		$.ajax({
        type: "POST",
        url: webpy2,
        data: { comm: comment },
        crossDomain: true,
        success:function(respons){
			//var resp = JSON.stringify(response);
			var resp = respons.response;
			if(resp=="obr"){
					lista[nr].firstElementChild.innerHTML  = "<strike>" + comment + "</strike>";
				}
			}
        });

}

	


