(ns clojure.examples.hello
    (:gen-class))
(defn hello-world []
    (def x 1)
    (def y 2)
    (def z (+ x y))
    ;; 
    (println z)
    (println "Hello World"))
(hello-world)