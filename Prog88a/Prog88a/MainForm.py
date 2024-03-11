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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Crimson
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(111, 37)
		self._label1.TabIndex = 0
		self._label1.Text = "Num1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(153, 18)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Crimson
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label2.Location = System.Drawing.Point(12, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(111, 37)
		self._label2.TabIndex = 2
		self._label2.Text = "Num2"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Crimson
		self._label3.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label3.Location = System.Drawing.Point(12, 103)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(111, 37)
		self._label3.TabIndex = 3
		self._label3.Text = "Sum"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Crimson
		self._label4.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label4.Location = System.Drawing.Point(12, 151)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(111, 37)
		self._label4.TabIndex = 4
		self._label4.Text = "Difference"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Crimson
		self._label5.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label5.Location = System.Drawing.Point(12, 198)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(111, 37)
		self._label5.TabIndex = 5
		self._label5.Text = "Product"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Crimson
		self._label6.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label6.Location = System.Drawing.Point(12, 246)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(111, 37)
		self._label6.TabIndex = 6
		self._label6.Text = "Average"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Crimson
		self._label7.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label7.Location = System.Drawing.Point(12, 294)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(111, 37)
		self._label7.TabIndex = 7
		self._label7.Text = "Distance"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Crimson
		self._label8.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label8.Location = System.Drawing.Point(12, 342)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(111, 37)
		self._label8.TabIndex = 8
		self._label8.Text = "Max"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Crimson
		self._label9.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label9.Location = System.Drawing.Point(12, 388)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(111, 36)
		self._label9.TabIndex = 9
		self._label9.Text = "Min"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(153, 65)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 10
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(278, 18)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(120, 122)
		self._button1.TabIndex = 18
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(278, 163)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(120, 118)
		self._button2.TabIndex = 19
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(278, 306)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(120, 118)
		self._button3.TabIndex = 20
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Pink
		self._label10.Location = System.Drawing.Point(153, 115)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 21
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Pink
		self._label11.Location = System.Drawing.Point(153, 163)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 22
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.Pink
		self._label12.Location = System.Drawing.Point(153, 210)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 23
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.Pink
		self._label13.Location = System.Drawing.Point(153, 258)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 24
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.Pink
		self._label14.Location = System.Drawing.Point(153, 306)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 25
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.Pink
		self._label15.Location = System.Drawing.Point(153, 354)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(100, 23)
		self._label15.TabIndex = 26
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.Pink
		self._label16.Location = System.Drawing.Point(153, 400)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(100, 23)
		self._label16.TabIndex = 27
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(410, 442)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Diff = num1 - num2
		Product = num1 * num2
		Average = Sum / 2.0
		AbsDiff = abs(Diff)
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:
			Max = num2
			
		if Max == num1:
			Min = num2
		else:
			Min = num1
			
		self._label10.Text = str(Sum)
		self._label11.Text = str(Diff)
		self._label12.Text = str(Product)
		self._label13.Text = str(Average)
		self._label14.Text = str(AbsDiff)
		self._label15.Text = str(Max)
		self._label16.Text = str(Min)
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""
		self._label15.Text = ""
		self._label16.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()