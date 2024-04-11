$(document).ready(function () { 
    let page = 1;
    document.addEventListener('wheel', function (e) {
        if (document.body.scrollTop === this.documentElement.scrollHeight - window.innerHeight && max >= page+1) {
            $.ajax({
                type: 'get',
                url: "",
                async: true,
                data: {'next_news': page+1, 'max': max},
                success: function (data) {
                    max = data['max'];
                    page += 1;
                    if (data["page"]==page) {
                        for (let news in data["news"]) {
                            news = data['news'][news];
                            document.getElementById('main').innerHTML += news;
                        }
                    }
                }
            });
        }
    });
});
