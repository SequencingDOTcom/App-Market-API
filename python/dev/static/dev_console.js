function addRow(tableID) {
    var table = document.getElementById(tableID);

    if (!table) return;

    var rows = table.rows.length;


    var newRow = table.rows[rows-1].cloneNode(true);

    // Now get the inputs and modify their names
    var inputs = newRow.getElementsByTagName('input');

    for (var i=0, iLen=inputs.length; i<iLen; i++) {
        // Update inputs[i]
    }

    // Add the new row to the tBody (required for IE)
    var tBody = table.tBodies[0];
    tBody.insertBefore(newRow, tBody.lastChild);
}

function deleteRow(tableID) {
    var table = document.getElementById(tableID);

    if (!table) return;

    var rows = table.rows.length;
    if (rows <= 1)
        return;

    table.deleteRow(rows-1);
}

function fileRetrievalTest() {
    var uriInput = document.getElementById('seq-gfr-uri-input');
    var seqAuthTokenInput = document.getElementById('seq-gfr-auth-token-input');
    var fileIdInput = document.getElementById('seq-gfr-file-id-input');
    var requestTextarea = document.getElementById('seq-gfr-req');
    var responseTextarea = document.getElementById('seq-gfr-resp');

    var uri = getInputValueOrDefaultPlaceholder(uriInput);
    var seqAuthToken = getInputValueOrDefaultPlaceholder(seqAuthTokenInput);
    var fileId = getInputValueOrDefaultPlaceholder(fileIdInput);

    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: '/dev/genetic_file_retrieval_test',
        data: {
            uri: uri,
            sequencingAuthenticationToken: seqAuthToken,
            id: fileId,
        },
        success: function (response) {
            requestTextarea.value = response.request;
            responseTextarea.value = response.response;
        },
        error: function (response) {
            requestTextarea.value = response.request;
            responseTextarea.value = response.response;
        }
    });

}

function seqJobStatusNotificationTest() {
    var uriInput = document.getElementById('seq-jsn-uri-input');
    var seqAuthTokenInput = document.getElementById('seq-jsn-auth-token-input');
    var seqJobIdInput = document.getElementById('seq-jsn-job-id-input');
    var processingStatusSelect = document.getElementById('seq-jsn-processing-status');
    var completionStatusSelect = document.getElementById('seq-jsn-completion-status');
    var errorMessageInput = document.getElementById('seq-jsn-error-message-input');
    var outputFilesTable = document.getElementById('seq-jsn-output-files-table');
    var attributesTable = document.getElementById('seq-jsn-attributes-table');
    var callbackList = document.getElementById('seq-jsn-callback-list').getElementsByTagName("li");
    var requestTextarea = document.getElementById('seq-jsn-req');
    var responseTextarea = document.getElementById('seq-jsn-resp');


    var uri = getInputValueOrDefaultPlaceholder(uriInput);
    var seqAuthToken = getInputValueOrDefaultPlaceholder(seqAuthTokenInput);
    var seqJobId = getInputValueOrDefaultPlaceholder(seqJobIdInput);
    var processingStatus = processingStatusSelect.value;
    var completionStatus = completionStatusSelect.value;
    var errorMessage = errorMessageInput.length != 0 ? errorMessageInput.value : null;

    var outputFiles = mapKeyValueTable(outputFilesTable);
    var attributes = mapKeyValueTable(attributesTable);
    var callback = {
        'url': callbackList[0].children[0].value,
        'username': callbackList[1].children[0].value,
        'password': callbackList[2].children[0].value,
    };

    console.log(outputFiles);
    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: '/dev/job_status_notification_test',
        data: {
            uri: uri,
            sequencingJobId: seqJobId,
            sequencingAuthenticationToken: seqAuthToken,
            status: processingStatus,
            completionStatus: completionStatus,
            errorMessage: errorMessage,
            outputFiles: JSON.stringify(outputFiles),
            attributes: JSON.stringify(attributes),
            callback: JSON.stringify(callback),
        },
        success: function (response) {
            requestTextarea.value = response.request;
            responseTextarea.value = response.response;
        },
        error: function (response) {
            requestTextarea.value = response.request;
            responseTextarea.value = response.responseText;
        }
    });
}

function getInputValueOrDefaultPlaceholder(input) {
    return input.value.length != 0 ? input.value : input.placeholder;
}

function mapKeyValueTable(table) {
    var map = {};
    for (var i = 0, row; row = table.rows[i]; i++) {
      var key = row.cells[0].children[0].value;
      var val = row.cells[1].children[0].value;
      map[key] = val;
    }
    return map;
}