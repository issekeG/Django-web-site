function loadnotebook(){
    $(".project").click(function (e){
        console.log("premiere");
         e.preventDefault();
		 e.stopPropagation();
         let project_id = $(this).attr("id")

        $.ajax({
            url : $("#sidebar-nav").attr("link-to-server-methode-url"),
            data : {
                'project_id':project_id,
            },
        })
            .done(function (response){
                $("#main").html(response);
                window.scrollTo(0, 0);

            })
            .fail(function (response){
                console.log("echec")
            })

    })
}
function loadnotebookbouton(){
    $(".projectbouton").click(function (e){
        console.log("deuxieme");
         e.preventDefault();
		 e.stopPropagation();
         var id ;
         let id_project = $(this).attr("id_project")

        $.ajax({
            url : $(this).attr("link-to-server-methode-url"),
            data : {
                'project_id':id_project,
            },
        })
            .done(function (response){
                $("#main").html(response);
                window.scrollTo(0, 0);

            })
            .fail(function (response){
                console.log("echec")
            })

    })
}