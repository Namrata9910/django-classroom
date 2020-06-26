const address = window.location;


$(document).ready(function() {
    console.log("i am ready");

    /**
    Hide the Django message after 3 seconds.
     */
    document.querySelectorAll("#messages").forEach(function(message) {
        setTimeout(function() {
            $(message).fadeOut("slow");
        }, 3000)
    });


    // $("#ota-link,#partners-link,#review-link").click(function(e) {
    //     e.preventDefault();
    //
    //     const this_ = $(this);
    //
    //     // Get the pathname in order to refer which data is to be fetched i.e ota or partner or review, etc
    //     let pathname = this_.attr("href").split("/");
    //
    //     // get the type of data to be fetched i.e ota or partner etc
    //     const dataType = pathname[pathname.length-2];
    //     console.log(dataType);
    //
    //     // Insert the 'j' at the to match the view data
    //     // Eg- /enquiry/j/ota/  or /enquiry/j/partner
    //     pathname.splice(2, 0, "j");
    //
    //     // Complete URL to fetch the data
    //     const contentFetchURL = address.origin + pathname.join("/");
    //     console.log(contentFetchURL);
    //
    //
    //     $.ajax({
    //         url: contentFetchURL,
    //         method: "GET",
    //         success: function(data) {
    //             // Change the title of the page
    //             document.title = `S3 Infosoft - ${dataType[0].toUpperCase() + dataType.substring(1)}`;
    //
    //             // Change the address of the page
    //             window.history.pushState(data, null, this_.attr("href"));
    //             $(".container-fluid").html(data);
    //         },
    //         error: function(err) {
    //             console.log(err);
    //         }
    //     })
    // });


    /**
     * Function to check whether the URL ends with any of the list contents
     * @param {Array} suffixes - The suffixes to check
     * @param {String} string - The string in which to check
     * @returns {boolean}
     */
    function urlEndsWith(suffixes, string) {
        return suffixes.some(function(suffix) {
            return string.endsWith(suffix) || string.includes(suffix);
        });
    }


    if (window.innerWidth > 768 && urlEndsWith(["/ota/", "/review/", "/partner/"], address.pathname)) {
        const anchorTag = $(".nav-link.collapsed.admin");
        const divTag = $("#collapseAdmin");
        anchorTag.removeClass("collapsed");
        divTag.addClass("show");
    }

    // Add the following code if you want the name of the file appear on select
    $(".custom-file-input").on("change", function() {
      let fileName = $(this).val().split("\\").pop();
      $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
    });
});

/**
 * Function to fetch the table contents from the API and attach them to the table.
 * @param {String} tableID - The table ID to attach the results
 * @param {String} apiPathname - The API pathname to send GET request
 * @param {Array} columns - The list of column names to attach data
 * @param {Array} customColumns - Extra settings for the column that doesn't apply to all pages
 */
function fetchTableDataFromAPI(tableID, apiPathname, columns, customColumns=[]) {
    console.log("Entered the calling function");
    $.ajax({
        url: address.origin + apiPathname,
        method: "GET",
        dataType: "json",
        success: function(data) {
            $(tableID).dataTable({
                "aaData": data,
                "aaSorting": [],    // disable the initial sorting
                "columns": columns,
                "order": [[0, "desc"]],
                "columnDefs": [
                    {

                        "targets": 1,
                        "render": function(data, type, row) {
                            let rowID = row["id"];

                            return `<a href="${rowID}/">${data.substring(0, 100)}</a>`
                        },
                    },

                    {
                        "targets": [0],
                        "visible": false,
                        "search": false,
                    },
                    ...customColumns
                ]
            });
        }
    })
}


/**
 * Add the newly created enquiry data to table
 * @param {String} tableID - Table ID to attach the result
 * @param {String} apiPathname - API pathname to send POST request
 * @param {JSON} formData - Data to send to API
 */
function addNewEnquiryData(tableID, apiPathname, formData) {

    $.ajax({
        url: address.origin + apiPathname,
        method: "POST",
        data: formData,
        dataType: "json",
        success: function(data) {
            console.log("Successfully created enquiry.");
            let table = $(tableID).DataTable();
            table.row.add(data).draw();
        },
        error: function(err) {
            console.log(err);
        }
    })
}


/**
 * Function to handle the form submission and clearing of form after AJAX
 * @param {String} formID - Form ID to handle its submission
 * @param {String} tableID - tableID - Table ID to attach the result
 * @param {String} apiPathname - API pathname to send POST request
 * @param {String} modalID - Modal ID too hide after submission
 */
function handleEnquiryFormSubmit(formID, tableID, apiPathname, modalID) {
    $(formID).submit(function(e) {
        e.preventDefault();
        const this_ = $(this);
        console.log("Creating enquiry.");
        addNewEnquiryData(tableID, apiPathname, this_.serialize());
        this_.trigger("reset");
        $(modalID).modal("hide");
    })
}


/**
 * Function to fetch the single instance of enquiry model from API
 * @param {String} fetch_url - URL to send GET request.
 * @param {Array} attachLocations - HTML elements on the page to attach data.
 * @param {Array} attachSequence - Sequence in which to attach the data.
 */
function fetchEnquiryInstanceData(fetch_url, attachLocations, attachSequence) {
    $.ajax({
        url: fetch_url,
        method: "GET",
        data: [],
        dataType: "json",
        success: data => {
            console.log("Data for a single instance of a enquiry model");
            for(let i=0; i<= attachLocations.length; i++) {
                $(attachLocations[i]).text(data[attachSequence[i]]);
            }
        },
        error: err => console.log(err),
    });
}


/**
 * Function to handle the updation and deletion of enquiry objects
 * @param {Object} instance - It is 'this' value of the form.
 * @param {Boolean} updation - If it is a updation.
 * @param {Boolean} deletion - If it is a deletion.
 *
 *
 * attachLocation, dataAttachSequence and afterDeleteURL are taken from the previous scope of the page.
 */
function objectUpdateDelete(instance, updation=false, deletion=false) {
    let data = null;
    let method = null;

    if (updation && !deletion) {
        data = instance.serialize();
        method = "PUT";
    } else if (deletion && !updation) {
        method = "DELETE";

    }

    const csrf = instance.find('[name="csrfmiddlewaretoken"').attr("value");

    $.ajax({
          url: api_address,
          method: method,
          headers: {"X-CSRFToken": csrf},
          data: data,
          dataType: "json",
          success: data => {
            console.log("successfull");
            if (updation) {
                updateElements(attachLocations, dataAttachSequence, data);
            } else if (deletion) {
                window.location = afterDeleteURL;
            }
          },
          error: err => console.log(err),
        });
}


/**
 * Function to update the elements text after the updation is successfull
 * @param attachLocations
 * @param attachSequence
 * @param data
 */
function updateElements(attachLocations, attachSequence, data) {
    for(let i=0; i<= attachLocations.length; i++) {
        $(attachLocations[i]).text(data[attachSequence[i]]);
    }
}


/**
 * Function to display and hide the alerts after a few seconds
 * @param {String} alertType- Type of alert i.e success, error, etc
 * @param {String} alertText- Text message to display in the alert.
 */
function displayAlert(alertType, alertText) {
    let alertID = $("#messages");
    let alertHTML = `<div class="alert alert-${alertType} text-center" role="alert">
        <button type="button" class="close" data-dismiss="alert">
          <span aria-hidden="true">&times;</span>
        </button>
        <span>${alertText}</span>
      </div>`;
    alertID.html(alertHTML);
    alertID.css("display", "");

    setTimeout(function() {
      alertID.fadeOut("slow");
    }, 3000);
}


/**
 * Function to convert the datetime string coming from API to dd-mm-yyyy HH:MM
 * @param {string} dateString - The string object that is to be converted
 * @param {boolean} only_date - Whether to return date only or include time also.
 * @returns {string}
 */
function formatDate(dateString, only_date=false) {
    let date = new Date(dateString);

    let day = date.getDate();
    let month = date.getMonth();
    let year = date.getFullYear();
    let hours = date.getHours();
    let minutes = date.getMinutes();

    if (only_date) {
        return `${day}/${month}/${year}`
    }

    return `${day}/${month}/${year} ${hours}:${minutes}`;

}
