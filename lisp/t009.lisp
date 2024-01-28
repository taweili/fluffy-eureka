;; SLIME Key bindings

;; C-c C-k Compile and load teh current buffer's file
;; C-c C-c Compile teh top-level form at point.

(+ 1 1)
(format t "Hello SLIME")

(defun test (x)
  (+ x x))

;; C-c C-d C-d Describe symbol
;; M-. Edit the definition of function at point
(test 100)

;; C-c C-] close all parans in sexp
(+ 2 (- 100 20))

;; C-C TAB complete symbol
