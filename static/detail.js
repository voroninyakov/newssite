form = document.getElementById('reaction-form');
likes = document.getElementById('likes');
dislikes = document.getElementById('dislikes');
if (form) {
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        $.ajax({
            type: 'post',
            url: "",
            async: true,
            data: { 'csrfmiddlewaretoken': csrftoken, 'like': event.submitter.value },
            success: function (data) {
                likes.innerText = data['likes_count'];
                dislikes.innerText = data['dislikes_count'];
            }
        });
    });
};