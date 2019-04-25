function download_url(filename, url)
{
    // Download file from a URL

    var link = document.createElement("a");
    link.download = filename;
    link.href = url;
    link.click();

}