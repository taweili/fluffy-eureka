(defmacro setq2 (v1 v2 e)
  (list 'progn (list 'setq v1 e) (list 'setq v2 e)))

(defparameter v1 1)
(defparameter v2 2)
(setq2 v1 v2 3)

(macroexpand '(setq2 v1 v2 3))
