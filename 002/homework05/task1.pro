sum(0, []).
sum(Total, [Head|Tail]) :- sum(Sum, Tail), Total is Head + Sum.

| ?- sum(What, [1, 2, 3]). % What = 6