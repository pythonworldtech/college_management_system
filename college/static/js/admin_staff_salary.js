$(document).ready(function() {
    $('.paywithrazorpay4').click(function(e) {
        e.preventDefault();

        var stf_id = $("[name='stf_id']").val();
        var staff_id = $("[name='staff_id']").val();
        var staff_name = $("[name='staff_name']").val();
        var salary = $("[name='salary']").val();
        var paid_salary = $("[name='paid_salary']").val();
        var due_salary = $("[name='due_salary']").val();
        var salary_to_paid = $("[name='salary_to_paid']").val();
        var remark = $("[name='remark']").val();
        var account_no = $("[name='account_no']").val();
        var ifsc = $("[name='ifsc']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();

        if (stf_id == "" || staff_id == "" || staff_name == "" || salary == "" || paid_salary == "" || due_salary == "" || remark == "" || salary_to_paid == "") {
            swal("Alert!", "All Fields are Required!", "error");
            return false;
        } else {
            $.ajax({
                success: function(response) {

                    var options = {
                        "key": "rzp_test_B7U0wWPKVCatGw",
                        "amount": salary_to_paid * 100,
                        "currency": "INR",
                        "name": "Python World",
                        "description": "Thank You For To visit Our Website",
                        "image": "https://drive.google.com/file/d/1yAPhJFqYshSaQ2k4VEiCM9qkkSFQTDF_/view?usp=sharing",
                        "handler": function(responseb) {
                            data = {
                                "stf_id": stf_id,
                                "staff_id": staff_id,
                                "salary": salary,
                                "staff_name": staff_name,
                                "due_salary": due_salary,
                                "paid_salary": paid_salary,
                                "salary_to_paid": salary_to_paid,
                                "remark": remark,
                                "account_no": account_no,
                                "ifsc": ifsc,
                                "payment_id": responseb.razorpay_payment_id,
                                csrfmiddlewaretoken: token

                            }
                            $.ajax({
                                method: "POST",
                                url: "/admin_proceed-to-pay2",
                                data: data,
                                success: function(responsec) {
                                    //console.log(responsec);
                                    swal("Congratulation!", responsec.status, "success").then((value) => {
                                        window.location.href = '/admin_view_staff_salary';
                                    });

                                }
                            });
                        },
                        "prefill": {
                            "name": staff_name,
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