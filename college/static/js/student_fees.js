$(document).ready(function() {
    $('.paywithrazorpay').click(function(e) {
        e.preventDefault();

        var admission_no = $("[name='admission_no']").val();
        var student_name = $("[name='student_name']").val();
        var course = $("[name='course']").val();
        var admission_fees = $("[name='admission_fees']").val();
        var paid_fees = $("[name='paid_fees']").val();
        var due_fees = $("[name='due_fees']").val();
        var fees = $("[name='fees']").val();
        var remark = $("[name='remark']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();

        if (admission_no == "" || student_name == "" || course == "" || admission_fees == "" || fees == "" || due_fees == "" || remark == "") {
            swal("Alert!", "All Fields are Required!", "error");
            return false;
        } else {
            $.ajax({
                success: function(response) {

                    var options = {
                        "key": "rzp_test_B7U0wWPKVCatGw",
                        "amount": fees * 100,
                        "currency": "INR",
                        "name": "Python World",
                        "description": "Thank You For To visit Our Website",
                        "image": "https://drive.google.com/file/d/1yAPhJFqYshSaQ2k4VEiCM9qkkSFQTDF_/view?usp=sharing",
                        "handler": function(responseb) {
                            data = {
                                "student_name": student_name,
                                "admission_no": admission_no,
                                "course": course,
                                "admission_fees": admission_fees,
                                "due_fees": due_fees,
                                "paid_fees": paid_fees,
                                "fees": fees,
                                "remark": remark,
                                "payment_id": responseb.razorpay_payment_id,
                                csrfmiddlewaretoken: token

                            }
                            $.ajax({
                                method: "POST",
                                url: "/proceed-to-pay",
                                data: data,
                                success: function(responsec) {
                                    //console.log(responsec);
                                    swal("Congratulation!", responsec.status, "success").then((value) => {
                                        window.location.href = '/student_fees';
                                    });

                                }
                            });
                        },
                        "prefill": {
                            "name": student_name,
                            "email": "gaurav.kumar@example.com",
                            "contact": "9999999999"
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();

                }
            });
        }
    });
});