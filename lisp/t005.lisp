(defclass person()
  ((name
    :initarg :name
    :accessor name)
   (lisper
    :initform nil
    :accessor lisper)))

(defvar p1 (make-instance 'person :name "John"))


