function upload_server(file, fileName, callback) {
    if (fileName.endsWith(".jar")) {
        var formData = new FormData();
        formData.append('fileStream', file);
        formData.append('fileName', fileName)
        this.$.ajax({
            url: '/upload_server_path',
            type: 'POST',
            cache: false,
            data: formData,
            processData: false,
            contentType: false
        }).done(function (res) {
            callback(res);
        }).fail(function (res) {
        });
    } else {
        callback("file-error");
    }
}


function query_submit_log() {
    this.$.ajax({
        url: '/while_query_submit',
        type: 'GET',
        cache: false,
        processData: false,
        contentType: false
    }).done(function (res) {
        document.getElementById("submit_info").value = res;
    }).fail(function (res) {
    });
}


function storm_submit_excute() {
    var formData = new FormData();
    formData.append('main_class', document.getElementById("main_class").value);
    formData.append('topo_name', document.getElementById("topo_name").value)
    formData.append('run_jar', document.getElementById("run_jar").value)
    $.ajax({
        url: '/submit_jar_execute',
        type: 'POST',
        cache: false,
        data: formData,
        processData: false,
        contentType: false
    }).done(function (res) {

    }).fail(function (res) {
    });

}