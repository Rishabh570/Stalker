$(document).ready(() => {
    console.log("Loaded!");

    $('#github-submit').click(() => {
            const input = $('#github-input').val();

            $.get('/stalk_on_github/', myData = {'filter': input}, (response) => {
                console.log(response);
                if(response === "success") {
                    alert(`you're now stalking ${input}`);
                }else {
                    console.log("failed");
                }
            });
    });

});
