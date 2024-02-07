(defn foo001 [a]
  (printf "foo001 %s%n" a)
  "foo001")

(defn foo002 [a]
  (printf "foo002 %s%n" a)
  "foo002")

(-> "foo000"
    (foo001)
    (foo002)
    (foo001))
