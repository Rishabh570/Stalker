$(document).ready(() => {
    console.log("Loaded!");


    $('#github-submit').click(() => {
            const input = $('#github-input').val();

            $.get('/stalk_on_github/', myData = {'filter': input}, (response) => {
                console.log('response is: ', response);

                for(i=0; i<response.length; i++) {
                    let type = response[i].type;
                    console.log(`type is: ${type} for ${i} turn`);

                    // Triggers when a repo is starred by victim
                    if(type === "WatchEvent") {
                        let piece = response[i].repo.url;
                        piece = piece.split('repos/')[1];
                        let repo_url = `https://github.com/${piece}`;

                        let t = response[i].created_at;
                        t = t.split('T')
                        let for_date = t[0];
                        let for_time = t[1].split(':');
                        let hours = parseInt(for_time[0]);
                        let minutes = parseInt(for_time[1]);
                        hours += 5;
                        minutes += 30;
                        console.log(hours, minutes);
                        if(hours >= 24 && minutes > 0){
                            console.log("inside");
                            hours -= 24;
                        }

                        const node = `<li style="display: none;" class='lead' id='github-report-${i}'><strong>Starred</strong> <a href='${repo_url}'><strong>${response[i].repo.name}</strong></a>` + ` at ${hours}:${minutes} on ${for_date}</p>` +'</li>';
                        
                        $('#report-place').append(node);
                        $(`#github-report-${i}`).fadeIn();
                        $('#github-remove').fadeIn();
                }
                // Triggers when victim pushes changes to any repo
                else if(type === "PushEvent") {
                    let piece = response[i].repo.url;
                    piece = piece.split('repos/')[1];
                    let repo_url = `https://github.com/${piece}`;                    

                    let t = response[i].created_at;
                    t = t.split('T')
                    let for_date = t[0];
                    let for_time = t[1].split(':');
                    let hours = parseInt(for_time[0]);
                    let minutes = parseInt(for_time[1]);
                    hours += 5;
                    minutes += 30;
                    console.log(hours, minutes);
                    if(hours >= 24 && minutes > 0){
                        console.log("inside");
                        hours -= 24;
                    }

                    let commits_num = response[i].payload.commits.length;
                    // Just some code to pluralize word "commit"
                    let is_commits;
                    if(commits_num > 1) {
                        is_commits = "commits";
                    }else {
                        is_commits = "commit";
                    }
                    // Building a URL from bits of info to show victim's commits
                    let commit_url = `https://github.com/${response[i].repo.name}/commits`;

                    const node = `<li style="display: none;" class="lead d-block mb-2" id="github-report-${i}"><strong>Pushed</strong> ${commits_num} <a href='${commit_url}'>${is_commits}</a> to <a href="${repo_url}">${response[i].repo.name}</a> at ${hours}:${minutes} on ${for_date}</li>`;

                    $('#report-place').append(node);
                    $(`#github-report-${i}`).fadeIn();
                    $('#github-remove').fadeIn();
                }


            } // For loop ends
            const button = '<button id="github-remove" style="display: none;" type="button" class="btn btn-dark">Stop Stalking</button>';
            $('#report-place').append(button);
        });

            $('.stalk-form').fadeToggle("slow");
            $('.report').fadeToggle();
    });

    $('#github-remove').click(() => {
        $.get('/remove-github/', (response) => {
            if (response === "success") {
                alert("You've lost your eyes on your victim :|");
            }
        })
    })

});