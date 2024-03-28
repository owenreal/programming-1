import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 31)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(173, 20)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 5)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Purchase Price"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(12, 90)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(173, 20)
		self._textBox2.TabIndex = 2
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 64)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Amount Recieved"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(13, 117)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Change Due"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 140)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(173, 20)
		self._label4.TabIndex = 5
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.SeaGreen
		self._label5.Location = System.Drawing.Point(12, 164)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(116, 23)
		self._label5.TabIndex = 6
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.SeaGreen
		self._label6.Location = System.Drawing.Point(12, 187)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(116, 23)
		self._label6.TabIndex = 7
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.SeaGreen
		self._label7.Location = System.Drawing.Point(12, 210)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(116, 23)
		self._label7.TabIndex = 8
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.SeaGreen
		self._label8.Location = System.Drawing.Point(12, 233)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(116, 23)
		self._label8.TabIndex = 9
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.SeaGreen
		self._label9.Location = System.Drawing.Point(12, 256)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(116, 23)
		self._label9.TabIndex = 10
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(219, 164)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 38)
		self._button1.TabIndex = 11
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(219, 210)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 38)
		self._button2.TabIndex = 12
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(219, 256)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 38)
		self._button3.TabIndex = 13
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label10
		# 
		self._label10.Location = System.Drawing.Point(134, 164)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(70, 23)
		self._label10.TabIndex = 14
		self._label10.Text = "Dollars"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label11
		# 
		self._label11.Location = System.Drawing.Point(134, 187)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(70, 23)
		self._label11.TabIndex = 15
		self._label11.Text = "Quarters"
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label12
		# 
		self._label12.Location = System.Drawing.Point(134, 210)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(70, 23)
		self._label12.TabIndex = 16
		self._label12.Text = "Dimes"
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label13
		# 
		self._label13.Location = System.Drawing.Point(134, 233)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(70, 23)
		self._label13.TabIndex = 17
		self._label13.Text = "Nickles"
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label14
		# 
		self._label14.Location = System.Drawing.Point(134, 256)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(70, 23)
		self._label14.TabIndex = 18
		self._label14.Text = "Pennies"
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(331, 318)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		purchase = float(self._textBox1.Text)
		recieved = float(self._textBox2.Text)
		change = recieved - purchase
		self._label4.Text = str(change)
		
		dollars = change // 1
		self._label5.Text = str(dollars)
		
		quarters = (change - dollars) // 0.25
		self._label6.Text = str(quarters)
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()