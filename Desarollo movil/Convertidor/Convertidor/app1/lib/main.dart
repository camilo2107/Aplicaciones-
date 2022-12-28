import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Convertidor',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Covertidor Monetario'),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

String op1 = "COP";
String op2 = "USD";
String op3 = "EUR";

class Calculadora {
  final titulo;
  final color;
  final icono;

  Calculadora(this.titulo, this.color, this.icono);
}

final txtOrigen = TextEditingController();
final txtDestino = TextEditingController();

List<DropdownMenuItem<String>> dd = <DropdownMenuItem<String>>[
  DropdownMenuItem(value: "USD", child: Text("USD")),
  DropdownMenuItem(value: "EUR", child: Text("EUR")),
  DropdownMenuItem(value: "COP", child: Text("COP")),
];

List<Calculadora> cal = <Calculadora>[
  Calculadora("9", Colors.teal, Icon(Icons.abc)),
  Calculadora("8", Colors.teal, Icon(Icons.abc)),
  Calculadora("7", Colors.teal, Icon(Icons.abc)),
  Calculadora("6", Colors.teal, Icon(Icons.abc)),
  Calculadora("5", Colors.teal, Icon(Icons.abc)),
  Calculadora("4", Colors.teal, Icon(Icons.abc)),
  Calculadora("3", Colors.teal, Icon(Icons.abc)),
  Calculadora("2", Colors.teal, Icon(Icons.abc)),
  Calculadora("1", Colors.teal, Icon(Icons.abc)),
  Calculadora("0", Colors.teal, Icon(Icons.abc)),
  Calculadora("Limpiar", Colors.teal, Icon(Icons.delete_outline)),
  Calculadora("Calcular", Colors.teal, Icon(Icons.calculate_outlined)),
];

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.title),
        ),
        body: Padding(
            padding: EdgeInsets.all(20),
            child: Column(
              children: [
                Row(
                  children: [
                    Text("Origen: "),
                    DropdownButton(
                        value: op1,
                        items: dd,
                        onChanged: (String? x) {
                          setState(() {
                            op1 = x.toString();
                          });
                        }),
                    VerticalDivider(),
                    VerticalDivider(),
                    VerticalDivider(),
                    Text("Destino: "),
                    DropdownButton(
                        value: op2,
                        items: dd,
                        onChanged: (String? x) {
                          setState(() {
                            op2 = x.toString();
                          });
                        }),
                  ],
                ),
                TextField(
                  controller: txtOrigen,
                  decoration: InputDecoration(
                      labelText: "Moneda Origen", hintText: "0"),
                ),
                TextField(
                  controller: txtDestino,
                  decoration: InputDecoration(
                      labelText: "Moneda Convertida", hintText: "0"),
                ),
                Expanded(
                  child: GridView.builder(
                    gridDelegate:
                        const SliverGridDelegateWithFixedCrossAxisCount(
                      crossAxisCount: 3,
                    ),
                    itemCount: cal.length,
                    itemBuilder: (BuildContext context, int index) {
                      return Card(
                        color: cal[index].color,
                        child: ListTile(
                          title: Center(
                            child: index > 9
                                ? cal[index].icono
                                : Text(cal[index].titulo),
                          ),
                          onTap: () {
                            if (index < 10) {
                              txtOrigen.text =
                                  txtOrigen.text + cal[index].titulo;
                            } else if (index == 10) {
                              txtOrigen.text = "";
                              txtDestino.text = "";
                            } else {
                              if (op1 == "USD" && op2 == "COP") {
                                txtDestino.text =
                                    (double.parse(txtOrigen.text) * 5000)
                                        .toString();
                              } else if (op1 == "COP" && op2 == "USD") {
                                txtDestino.text =
                                    (double.parse(txtOrigen.text) / 5000)
                                        .toString();
                              } else if (op1 == "EUR" && op2 == "COP") {
                                txtDestino.text =
                                    (double.parse(txtOrigen.text) * 5100)
                                        .toString();
                              } else if (op1 == "COP" && op2 == "EUR") {
                                txtDestino.text =
                                    (double.parse(txtOrigen.text) / 5100)
                                        .toString();
                              } else if (op1 == "EUR" && op2 == "USD") {
                                txtDestino.text =
                                    (double.parse(txtOrigen.text) * 1.1)
                                        .toString();
                              } else if (op1 == "USD" && op2 == "EUR") {
                                txtDestino.text =
                                    (double.parse(txtOrigen.text) / 1.1)
                                        .toString();
                              } else {
                                txtDestino.text = txtOrigen.text;
                              }
                            }
                            print(cal[index].titulo);
                          },
                        ),
                      );
                    },
                  ),
                )
              ],
            )));
  }
}
