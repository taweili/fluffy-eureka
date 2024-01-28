(require 'cl-http)

(defun send-post-request (url data)
  "Make a POST request and return the response."
  (let ((response (http-request url :method :post
                                :headers '(("Content-Type" . "application/json")
                                           ("Authorization" . "Bearer YOUR_TOKEN"))
                                :body data)))
    (cl-http-parse-response response)))
