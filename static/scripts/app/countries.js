$(document).ready(function () {
    $("#summary_table").tablesorter();
    $("#summary_table").tablesorter({ sortList: [[0, 0], [1, 0]] });
});

$('#search_summary').keyup(function () {
    var searchStr = $(this).val();
    searchStr = searchStr.toLowerCase();
    var total = 0;
    $("#summary_table tr").each(function (index) {
        if (!index) return;
        var country = $(this).find("td").eq(1).text().toLowerCase();
        if (country.indexOf(searchStr) !== -1) {
            $(this).toggle(true);
            total++;
        }
        else
            $(this).toggle(false);
    });
    $("#summarycount").text(" " + total + " results");
});
