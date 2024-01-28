(defn foo001 [a]
  (println "foo001 %s " a)
  1)

(defn foo002 [a]
  (println "foo002 %s" a)
  2)

(-> 10
    (foo001)
    (foo002))
