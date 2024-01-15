(ql:quickload :drakma)
(ql:quickload :cl-json)

(drakma:http-request "http://lisp.org/")

(drakma:http-request "http://localhost:11434/api/generate"
                     :method :post
                     :content (json:encode-json-to-string
                               '(("model" . "mistral")
                                 ("prompt" . "why is sky blue?"))))

(json:encode-json '((model . mistral)))

