(require 'ellama)

(ellama-stream "Write a elisp code to split a string into list"
               :on-done 'got-code)
(defun got-code (text)
  (message "GOT-CODE"))
