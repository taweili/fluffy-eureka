(ignore-errors
 (/ 3 0))

(handler-case (/ 3 0)
  (error (c)
    (format t "Caught a condition. ~&")
    (values 0 c)))

