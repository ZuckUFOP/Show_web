function clique(resposta){
	var x=window.location.href;
	var r=confirm("Você está certo disso?");
	var y;
	var z;
	if (r){
		if (resposta=="True"){
			alert("Voce Acertou");
			y = x.substring(0,x.length-2);
			z = x.substring(x.length-1,x.length-2);
			if (z < 4){
				z=Number(z)+1;
				window.location.replace(y+z.toString()+'/');
			}
			else{
				window.location.replace("/polls/vitoria/");
			}
		}
		else{
			alert("Voce Errou");
			window.location.replace("/polls/voce_perdeu/");
		}
	}
}

function entrada (botao) {
	botao.className = "destacado";
}

function saida (botao){
	botao.className = "normal";
}