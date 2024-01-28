(ql:quickload "bordeaux-threads")

(bt2:all-threads)

(bt2:current-thread)

(bt2:thread-name (bt2:current-thread))
