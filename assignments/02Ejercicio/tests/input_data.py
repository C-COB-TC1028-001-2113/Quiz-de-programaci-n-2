# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["640","751","954"],
            ["","","","954 751 640"],
            "Revisa tu código",
        ),
        # Test case 2
        (
            ["-5","-24","95"],
            ["","","","95 -5 -24"],
            "Revisa tu código",
        ),
        # Test case 3
        (
            ["15","75","64"],
            ["","","","75 64 15"],
            "Revisa tu código",
        ),
        # Test case 4
        (
            ["25","2","74"],
            ["","","","74 25 2"],
            "Revisa tu código",
        ),
    ]
