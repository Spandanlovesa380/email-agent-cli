function doPost(e) {
    const data = JSON.parse(e.postData.contents);

    GmailApp.sendEmail(
        data.to,
        data.subject,
        data.body
    );

    return ContentService
        .createTextOutput(
            JSON.stringify({
                success: true
            })
        )
        .setMimeType(ContentService.MimeType.JSON);
}