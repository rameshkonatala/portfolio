$(function()   {
    $(".link").click(function(e) {
        e.preventDefault();
        $('div.panel:visible').hide();
        $(this).next('div.panel').show();
    });
});
