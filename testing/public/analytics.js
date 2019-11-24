window.onload = function() {
    var reason = document.getElementById('top-reason');
    var total = document.getElementById('times-cried');

    // Track the frequency of each issue
    var bellyache = 0,
        discomfort = 0,
        burping = 0,
        tired = 0,
        hungry = 0;

    $.ajax({
        url: 'http://localhost:8080/',
        method: 'GET',
        success: (item) => {
            item.forEach((taskData) => {
                if (taskData.Task_Name == "Bellyache") {
                    bellyache = bellyache + 1;
                } else if (taskData.Task_Name == "Discomfort") {
                    discomfort = discomfort + 1;
                } else if (taskData.Task_Name == "Burping") {
                    burping = burping + 1;
                } else if (taskData.Task_Name == "Tired") {
                    tired = tired + 1;
                } else if (taskData.Task_Name == "Hungry") {
                    hungry = hungry + 1;
                }
            });
            var arr = [bellyache, discomfort, burping, tired, hungry];

            Array.prototype.max = function(){
                return Math.max.apply(null, this);
            };

            if(arr.max() == bellyache){
                reason.innerHTML = "Bellyache";
            }
            else if(arr.max() == discomfort){
                reason.innerHTML = "Discomfort";
            }
            else if(arr.max() == burping){
                reason.innerHTML = "Burping";
            }
            else if(arr.max() == tired){
                reason.innerHTML = "Tired";
            }
            else if(arr.max() == hungry){
                reason.innerHTML = "Hungry";
            }

            total.innerHTML = bellyache + discomfort + burping + tired + hungry;

        }
    });
};