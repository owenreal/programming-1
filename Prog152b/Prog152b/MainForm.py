import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Salmon
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Test Value:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(119, 11)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 36)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(282, 277)
		self._listBox1.TabIndex = 2
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 319)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 32)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(119, 319)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 32)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(220, 319)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 32)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(307, 363)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		testValue = self._textBox1.Text		
		heading1 = "Test Value: " + str(testValue)
		heading2 = "Even Integer\tSum"
		self._listBox1.Items.Add(heading1)
		self._listBox1.Items.Add(heading2)
		
		for num in range(0, int(testValue) + 1, 2):
			lastnum = num
			Sum = lastnum
			if Sum < testValue:
				Sum = lastnum + num
				msg = str(num) + "\t\t" + str(Sum)
				self._listBox1.Items.Add(msg)
				
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()