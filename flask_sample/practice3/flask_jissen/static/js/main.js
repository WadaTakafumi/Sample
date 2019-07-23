
$(function () {
    //console.log("this is some debug information");
    //$('#numberOfTodos').text(3);

    //let todos = ["起きる", "朝ごはんを食べる", "学校に行く"];

    //$.each(todos, function(index, value) {
    //	$("#todoList").append($('<li/>', {text: value})); // <li>{value}<li>
    //});


    $.get("http://localhost:5000/getNumberOfTodos", function (numberOfTodos) {
        console.log("received '" + numberOfTodos + "' from server");
        $('#numberOfTodos').text(numberOfTodos);
        //$('#todolist').append($('<li/>', {text: value}));
    });

    $.get("http://localhost:5000/todolist", function (todos) {
        //console.log("received '" + todoList + "' from server" );

        $.each(todos, function (index, todo) {
            $("#todoList").append($('<li/>', { text: todo.content, class: todo.done ? "done" : "" })); // <li>{value}<li>
        });
    });
})
