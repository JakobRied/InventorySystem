$(document).ready(function () {

  $("#submitItem").on("click", function (e) {
    e.preventDefault();
    $.ajax({
      data: {
        item_name: $("#item_name").val(),
      },
      type: "POST",
      url: "/dub-items/",
    }).done(function (data) {
      if (data.output) {
        $("#item_form").submit();
        console.log(data.output);
      } else {
        alert("This Name is already used, please choose other one.");
      }
    });
  });

  $("#item_form").submit(function (e) {
    if (!$("#item_name").val()) {
      e.preventDefault();
      alert("Please fill the Item Name first");
    }
  });

  $("#submitBike").on("click", function (e) {
    e.preventDefault();
    $.ajax({
      data: {
        bike_name: $("#bike_name").val(),
      },
      type: "POST",
      url: "/dub-bikes/",
    }).done(function (data) {
      if (data.output) {
        $("#bike_form").submit();
        console.log(data.output);
      } else {
        alert("This Name is already used, please choose other one.");
      }
    });
  });


  $("#submitDelay").on("click", function (e) {
    e.preventDefault();
    $("#delay_form").submit();
  });

  $("#delay_form").submit(function (e) {
    if (!$("#reason").val()) {
      e.preventDefault();
      alert("Please fill the Bike Name first");
    }
  });

});