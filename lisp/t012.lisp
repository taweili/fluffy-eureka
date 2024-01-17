(defun divide (x y)
    (assert (not (zerop y))
        (y)
        "Division by zero is not allowed.")
    (/ x y))

(divide 1 0)
