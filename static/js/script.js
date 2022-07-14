// function link(){
//   document.getElementById("text").innerText = "変更しました";
// }

$(function(){
    $('#submit').click(function(){
        $("#text").html("変更したよ！");
    })
})