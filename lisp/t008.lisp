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

(defvar gen_res_str (flexi-streams:octets-to-string gen_res :external-format :utf-8))
(str:join "" (loop for x in (str:lines gen_res_str)
                   collect (cdr (assoc :RESPONSE (json:decode-json-from-string x)))))

;;;
(dex:get "http://localhost:11434/api/tags"
         :verbose t)
