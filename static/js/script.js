$(document).ready(function(){
    //alert("page load success");
});

$("#check_task").click(function(){
    var task_id = $("#task_id").val();
    var pd = {"task_id":task_id};
    $.ajax({
        type:"post",
        url:"/index",
        data:pd,
        cache:false,
        //success:function(data){
        //    alert(data);
        //},
        //error:function(){
        //    alert("error!");
        //},
    });
});

$("#login").click(function(){
    var user = $("#username").val();
    var pwd = $("#password").val();
    var pd = {"username":user, "password":pwd};
    $.ajax({
        type:"post",
        url:"/",
        data:pd,
        cache:false,
        //success:function(data){
        //    alert(data);
        //},
        //error:function(){
        //    alert("error!");
        //},
    });
});
