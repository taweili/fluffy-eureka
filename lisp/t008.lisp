(ql:quickload :dexador)
(ql:quickload :cl-json)
(ql:quickload :flexi-streams)
(ql:quickload :str)

(defvar gen_res (dex:post "http://localhost:11434/api/generate"
                          :headers '(("content-type" . "application/json"))
                          :verbose t
                          :content (json:encode-json-to-string
                                    '(("model" . "mistral")
                                      ("stream" . nil)
                                      ("prompt" . "What is the name of capital of China?")))))

(multiple-value-bind (body status headers uri stream)
    (dex:post "http://localhost:11434/api/generate"
              :headers '(("content-type" . "application/json"))
              :verbose t
              :want-stream t
              :content (json:encode-json-to-string
                        '(("model" . "mistral")
                          ("stream" . t)
                          ("prompt" . "What's the capital city of China?"))))
  (let (stream)
    (setq stream (flexi-streams:make-flexi-stream body :external-format :utf-8))
    (setq content (str:join "" (loop for line = (read-line stream nil)
                       until (eq line nil)
                       collect (cdr (assoc :RESPONSE (json:decode-json-from-string line))))))
    (format t "~s ~%" content)))

(defvar ollama-stream (dex:post "http://localhost:11434/api/generate"
                         :headers '(("content-type" . "application/json"))
                         :verbose t
                         :want-stream t
                         :content (json:encode-json-to-string
                                   '(("model" . "mistral")
                                     ("stream" . t)
                                     ("prompt" . "What's the capital city of China?")))))
(format t "Type: ~s ~%" ollama-stream)

(defvar gen_res_str (flexi-streams:octets-to-string gen_res :external-format :utf-8))
(str:join "" (loop for x in (str:lines gen_res_str)
                   collect (cdr (assoc :RESPONSE (json:decode-json-from-string x)))))

;;;
(dex:get "http://localhost:11434/api/tags"
         :verbose t)

(defun ollama-generate (model prompt)
  (let ((stream) (body))
    (setq body (dex:post "http://localhost:11434/api/generate"
                           :headers '(("content-type" . "application/json"))
                           :verbose nil
                           :want-stream t
                           :content (json:encode-json-to-string
                                     (list (cons "model" model)
                                           (cons "stream" t)
                                           (cons "prompt" prompt)))))
    (setq stream (flexi-streams:make-flexi-stream body :external-format :utf-8))
    (str:join "" (loop for line = (read-line stream nil)
                       until (eq line nil)
                       collect (cdr (assoc :RESPONSE (json:decode-json-from-string line)))))))

