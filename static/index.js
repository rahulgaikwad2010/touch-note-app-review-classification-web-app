document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#form').onsubmit = (event) => {

        event.preventDefault();
        document.querySelector('#search_result').innerHTML="";

        var formData = $('#form').serializeArray();
        var indexed_array = {};

        $.map(formData, function(n, i){
            indexed_array[n["name"]] = n["value"];
        });

        // Initialize new request
        const request = new XMLHttpRequest();
        request.open('POST', '/');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);
			const status = JSON.parse(request.status);

            // Update the result div
            if (status == 200) {
                if (data.prediction == "positive"){
                    var input_textbox = '<div class="alert alert-success" role="alert"><label for="exampleInputEmail1">Predicted Sentiment</label> <input class="form-control" type="text" placeholder="'+data.prediction.toUpperCase()+'" readonly></div>';
                }
                else{
                    var input_textbox = '<div class="alert alert-danger" role="alert"><label for="exampleInputEmail1">Predicted Sentiment</label> <input class="form-control" type="text" placeholder="'+data.prediction.toUpperCase()+'" readonly></div>';
                }

                document.getElementById("search_result").innerHTML=input_textbox;
            }
            else if(status == 410) {
				var input_textbox = '<div class="alert alert-danger" role="alert"><label for="exampleInputEmail1">Predicted Sentiment</label> <input class="form-control" type="text" placeholder="'+data.message+'" readonly></div>';
				document.getElementById("search_result").innerHTML=input_textbox;
            }
			else {
				var input_textbox = '<div class="alert alert-success" role="alert"><label for="exampleInputEmail1">Predicted Sentiment</label> <input class="form-control" type="text" placeholder="Others" readonly></div>';
				document.getElementById("search_result").innerHTML=input_textbox;
			}
        }

        // Add data to send with request
        const data = new FormData();
        data.append('FormData', JSON.stringify(indexed_array));

        // Send request
        request.send(data);
        return false;
    };
});