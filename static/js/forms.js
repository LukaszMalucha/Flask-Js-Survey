

Survey
    .StylesManager
    .applyTheme("default");
    var questions_data = questions;
    var answers_data = answers;
    $('#algorithm_results').hide();

var json = {
    title: "Characterize your Data task to find out what's the most suitable algorithm.",
    showProgressBar: "bottom",
    pages: [
        {

            questions: [
                {
                    type: "radiogroup",
                    name: "question1",
                    title: questions_data[0],
                    isRequired: true,
                    choices: answers_data[0]
                }
            ]
        },
        {

            questions: [
                {
                    type: "radiogroup",
                    name: "question2",
                    title: questions_data[1],
                    isRequired: true,
                    choices: answers_data[1]
                }
            ]
        },
         {

            questions: [
                {
                    type: "radiogroup",
                    name: "question3",
                    title: questions_data[2],
                    isRequired: true,
                    choices: answers_data[2]
                }
            ]
        },
         {

            questions: [
                {
                    type: "radiogroup",
                    name: "question4",
                    title: questions_data[3],
                    isRequired: true,
                    choices: answers_data[3]
                }
            ]
        },
         {

            questions: [
                {
                    type: "radiogroup",
                    name: "question5",
                    title: questions_data[4],
                    isRequired: true,
                    choices: answers_data[4]
                }
            ]
        },

    ]
};

window.survey = new Survey.Model(json);
survey.requiredText = ":"; survey.render();

survey
    .onComplete

    .add(function (result) {
            $.ajax({
                dataType: 'json',
                contentType: 'application/json',
                type : 'POST',
                url : '/results',
                data : JSON.stringify(result.data),

            })

            .done(function(data) {
                 $('#algorithm_results').show();
                 $('#results').text(data.result).show();
            });

    });


$("#surveyElement").Survey({model: survey});

function animate(animitionType, duration) {
    if (!duration)
        duration = 400;
    var element = document.getElementById("surveyElement");
    $(element).velocity(animitionType, {duration: duration});
}

var doAnimantion = true;
survey
    .onCurrentPageChanging
    .add(function (sender, options) {
        if (!doAnimantion)
            return;
        options.allowChanging = false;
        setTimeout(function () {
            doAnimantion = false;
            sender.currentPage = options.newCurrentPage;
            doAnimantion = true;
        }, 400);
        animate("fadeOut", 400);
    });
survey
    .onCurrentPageChanged
    .add(function (sender) {
        animate("fadeIn", 400);
    });
survey
    .onCompleting
    .add(function (sender, options) {
        if (!doAnimantion)
            return;
        options.allowComplete = false;
        setTimeout(function () {
            doAnimantion = false;
            sender.doComplete();
            doAnimantion = true;
        }, 400);
        animate("fadeOut", 400);
    });
animate("fadeIn", 400);