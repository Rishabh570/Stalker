$(document).ready(() => {
    console.log("dashboard script launched!");

    $('#github-report').click(() => {
        $('#github-report').fadeToggle();
        $.get('/github-report/', (response) => {
            let type = response[0].type;
            if(type === "WatchEvent") {
                let check = $('#github-report-blob').length;
                if(check === 0) {
                    const node = `<li style="display: none;" class='lead' id='github-report-blob'>${response[0].actor.login} starred <strong>${response[0].repo.name}</strong></p>` +`<p>Link is : <strong>${response[0].repo.url}</strong></li>`
                    $('#report-place').append(node);
                    $('#github-report-blob').fadeIn();
                }
            }
        });
    });





})