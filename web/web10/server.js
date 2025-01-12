import { createServer } from "http";
import { readFile } from "fs";
   
createServer(function(request, response){
       
    let filePath = "index.html";
    if(request.url !== "/"){

        filePath = request.url.substring(1);
    }
    readFile(filePath, function(error, data){
               
        if(error){
                   
            response.statusCode = 404;
            response.end("Resourse not found!");
        }   
        else{
            response.end(data);
        }
    });
     
}).listen(3000, function(){
    console.log("Server started at 3000");
});