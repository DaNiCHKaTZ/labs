import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [rows, setRows] = useState([]);
  const [name, setName] = useState('');
  const [quantity, setQuantity] = useState('');
  const [price, setPrice] = useState('');
  const [totalSum, setTotalSum] = useState(0);
  const [isEditing, setIsEditing] = useState(false);
  const [editingIndex, setEditingIndex] = useState(null);

  const addRow = () => {
    if (!name || quantity <= 0 || price <= 0) {
      alert('Пожалуйста, введите корректные данные. Количество и цена должны быть положительными числами.');
      return;
    }

    const newRow = {
      name: name,
      quantity: parseFloat(quantity),
      price: parseFloat(price),
      sum: (quantity * price).toFixed(2)
    };

    if (isEditing) {
      const updatedRows = rows.map((row, index) =>
        index === editingIndex ? newRow : row
      );
      setRows(updatedRows);
      setIsEditing(false);
      setEditingIndex(null);
    } else {
      setRows([...rows, newRow]);
    }

    setName('');
    setQuantity('');
    setPrice('');
  };

  const editRow = (index) => {
    const row = rows[index];
    setName(row.name);
    setQuantity(row.quantity);
    setPrice(row.price);
    setIsEditing(true);
    setEditingIndex(index);
  };

  const deleteRow = (index) => {
    const updatedRows = rows.filter((_, i) => i !== index);
    setRows(updatedRows);
  };

  useEffect(() => {
    const total = rows.reduce((acc, row) => acc + parseFloat(row.sum), 0);
    setTotalSum(total.toFixed(2));
  }, [rows]);

  return (
    <div className="App">
      <div>Список продуктов</div>
      <table>
        <thead>
          <tr>
            <th>Название</th>
            <th>Количество</th>
            <th>Цена</th>
            <th>Сумма</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row, index) => (
            <tr key={index} onDoubleClick={() => editRow(index)}>
              <td>{row.name}</td>
              <td>{row.quantity}</td>
              <td>{row.price}</td>
              <td>{row.sum}</td>
              <td>
                <button onClick={() => deleteRow(index)}>Удалить</button>
                <button onClick={() => editRow(index)}>Редактировать</button>
              </td>
            </tr>
          ))}
          <tr>
            <td colSpan="3"><strong>Общая сумма</strong></td>
            <td><strong>{totalSum}</strong></td>
            <td></td>
          </tr>
        </tbody>
      </table>
      <div>
        <input
          type="text"
          placeholder="Название"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="number"
          placeholder="Количество"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          min="1"
        />
        <input
          type="number"
          placeholder="Цена"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          min="0.01"
        />
        <button onClick={addRow}>
          {isEditing ? 'Сохранить изменения' : 'Добавить строку'}
        </button>
      </div>
    </div>
  );
}

export default App;
